import * as Skandha from 'skandha';
import { Highlight, Selection } from 'skandha-facets';
import { BlogT } from '/src/api/types';
import { registerBlogsCtr } from '/src/blogs/BlogsState/registerBlogsCtr';
import { BlogsData } from '/src/blogs/facets/BlogsData';

export type PropsT = {
  getBlogs: () => BlogT[];
};

export class BlogsState {
  props: PropsT;

  blogsCtr = {
    data: new BlogsData(),
    highlight: new Highlight<BlogT>(),
    selection: new Selection<BlogT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerBlogsCtr(this);
  }
}
