import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import {
  Deletion,
  Edit,
  Selection,
  handleSelectItem,
  topOfTheList,
} from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { BlogPostT } from '/src/api/types';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';
import { ObjT } from '/src/utils/types';

const mapData = (state: BlogPostsState) => {
  const ctr = state.blogPostsCtr;
  const getBlogPostById = (x: string | undefined) =>
    x ? ctr.data.blogPostById[x] : undefined;

  mapDataToProps(ctr, {
    data: {
      blogPosts: () => state.props.getBlogPosts(),
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.blogPosts),
      items: () =>
        ctr.selection.itemIds
          .map(getBlogPostById)
          .filter((x?: BlogPostT) => !!x) as BlogPostT[],
    },
    highlight: {
      highlightableIds: () => R.map(R.prop('id'), ctr.data.blogPosts),
      item: () => getBlogPostById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: BlogPostsState) => {
  const ctr = state.blogPostsCtr;

  ctr.addition.callbackMap = {
    add: {
      stageAdd() {
        ctr.addition.parentId = ctr.highlight.itemId || topOfTheList;
      },
      highlightNewItem() {
        ctr.selection.selectItem({ itemId: ctr.addition.item?.id });
        ctr.edit.enable();
      },
    },
    cancel: {
      unstageAdd(parentId: string | undefined) {
        ctr.edit.cancel();
        // The UI will restore the previous url
      },
    },
    confirm: {
      confirmAdd() {},
    },
  };

  ctr.deletion.callbackMap = {
    delete: {
      deleteItems(this: Cbs<Deletion['delete']>) {
        return state.props.deleteBlogPosts(this.args.itemIds);
      },
    },
  };

  ctr.edit.callbackMap = {
    save: {
      saveItem(this: Cbs<Edit['save']>) {
        return state.props
          .saveBlogPost(this.args.values)
          .then((response: ObjT) => {
            ctr.addition.confirm();
            return response;
          });
      },
    },
    cancel: {
      onCancel() {
        ctr.addition.cancel();
      },
    },
  };

  ctr.selection.callbackMap = {
    selectItem: {
      selectItem(this: Cbs<Selection['selectItem']>) {
        handleSelectItem(ctr.selection, this.args);
        if (!this.args.isCtrl && !this.args.isShift) {
          ctr.highlight.set({ itemId: this.args.itemId });
        }
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
