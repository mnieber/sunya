import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import {
  Edit,
  Selection,
  handleSelectItem,
  topOfTheList,
} from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { BlogsState } from '/src/blogs/BlogsState';
import { ObjT } from '/src/utils/types';

const mapData = (state: BlogsState) => {
  const ctr = state.blogsCtr;
  const getBlogById = (x: string) => ctr.data.blogById[x];

  mapDataToProps(ctr, {
    data: {
      blogs: () => state.props.getBlogs(),
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.blogs),
    },
    highlight: {
      item: () =>
        ctr.highlight.itemId ? getBlogById(ctr.highlight.itemId) : undefined,
    },
  });
};

const setCallbacks = (state: BlogsState) => {
  const ctr = state.blogsCtr;

  ctr.addition.callbackMap = {
    add: {
      stageAdd() {
        ctr.addition.parentId = topOfTheList;
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

  ctr.edit.callbackMap = {
    save: {
      saveItem(this: Cbs<Edit['save']>) {
        return state.props.saveBlog(this.args.values).then((response: ObjT) => {
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

export const registerBlogsCtr = (state: BlogsState) => {
  registerCtr({
    ctr: state.blogsCtr,
    options: { name: 'BlogsState.Blogs' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
