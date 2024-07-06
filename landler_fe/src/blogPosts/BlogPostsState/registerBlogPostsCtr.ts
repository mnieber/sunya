/*
The registerBlogPostsCtr function registers the blogPostsCtr container with the BlogPostsState:

- It calls mapData to connect the inputs and outputs of each facet. For example, the filteredBlogPosts
output of the data facet is connected to the selectableIds input of the selection);
- It calls setCallbacks to implement the callbacks of each facet. For example, the deleteItems callback
of deletion.delete is implemented by calling the deleteBlogPosts property of the BlogPostsState.

The setCallbacks function is also used to create interactions between the behaviours. For example,
when the filter is enabled, the highlight is corrected.

Note that because we are using the registerCtr function from skandha-mobx (instead of using the one
from skandha) the facets in blogPostsCtr are observable with MobX.
*/

import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Deletion, Selection, handleSelectItem } from 'skandha-facets';
import { correctHighlight } from 'skandha-facets/policies';
import { registerCtr } from 'skandha-mobx';
import { BlogPostT } from '/src/api/types';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';

const mapData = (state: BlogPostsState) => {
  const ctr = state.blogPostsCtr;
  const getBlogPostById = (x: string) => ctr.data.blogPostById[x];

  mapDataToProps(ctr, {
    // The inputs for 'filtering' is the list of the blogPosts.
    filtering: {
      inputItems: () => ctr.data.blogPosts,
    },
    // We set the output of 'filtering' to 'data.filteredBlogPosts'.
    data: {
      blogPosts: () => state.props.getBlogPosts(),
      filteredBlogPosts: () => ctr.filtering.filteredItems,
    },
    // The filtered blogPosts can be selected.
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.filteredBlogPosts),
    },
    // We look up the highlighted item by 'highlight.itemId'.
    highlight: {
      item: () =>
        ctr.highlight.itemId
          ? getBlogPostById(ctr.highlight.itemId)
          : undefined,
    },
  });
};

const setCallbacks = (state: BlogPostsState) => {
  const ctr = state.blogPostsCtr;

  ctr.deletion.callbackMap = {
    delete: {
      deleteItems(this: Cbs<Deletion['delete']>) {
        return state.props.deleteBlogPosts(this.args.itemIds);
      },
    },
  };

  ctr.selection.callbackMap = {
    // Here we implement the callbacks of the Selection.selectItem function.
    selectItem: {
      // Implement the 'selectItem' callback.
      selectItem(this: Cbs<Selection['selectItem']>) {
        // Perform the selection
        handleSelectItem(ctr.selection, this.args);
        // Apply the policy that highlight follows selection
        if (!this.args.isCtrl && !this.args.isShift) {
          ctr.highlight.set({ itemId: this.args.itemId });
        }
      },
    },
  };

  ctr.filtering.callbackMap = {
    // Here we implement the callbacks of the Filtering.setEnabled function.
    setEnabled: {
      // Implement the 'exit' callback. This is a special callback that is
      // called automatically when the Filtering.setEnabled function exits.
      exit() {
        // When exiting 'setEnabled' we make a correction to the highlight
        // if it points to an item that is filtered out.
        correctHighlight(
          ctr.highlight,
          (ctr.filtering.inputItems ?? []).map((x: BlogPostT) => x.id),
          ctr.filtering.filteredItems.map((x: BlogPostT) => x.id)
        );
      },
    },
  };
};

export const registerBlogPostsCtr = (state: BlogPostsState) => {
  registerCtr({
    ctr: state.blogPostsCtr,
    options: { name: 'BlogPostsState.BlogPosts' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
