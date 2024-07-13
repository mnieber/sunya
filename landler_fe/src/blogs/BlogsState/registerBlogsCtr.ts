import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Selection, handleSelectItem } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { BlogsState } from '/src/blogs/BlogsState';

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
