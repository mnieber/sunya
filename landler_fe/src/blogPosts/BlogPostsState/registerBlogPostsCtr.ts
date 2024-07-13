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
    filtering: {
      inputItems: () => ctr.data.blogPosts,
    },
    data: {
      blogPosts: () => state.props.getBlogPosts(),
      filteredBlogPosts: () => ctr.filtering.filteredItems,
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.filteredBlogPosts),
    },
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
