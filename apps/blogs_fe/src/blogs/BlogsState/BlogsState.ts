import * as Skandha from 'skandha';
import { Addition, Edit, Highlight, Selection } from 'skandha-facets';
import { BlogT } from '/src/api/types';
import { BlogsData } from '/src/blogs/BlogsState/facets/BlogsData';
import { registerBlogsCtr } from '/src/blogs/BlogsState/registerBlogsCtr';
import { ObjT } from '/src/utils/types';

export type PropsT = {
  getBlogs: () => BlogT[];
  saveBlog: (values: ObjT) => Promise<any>;
};

export class BlogsState {
  props: PropsT;

  blogsCtr = {
    data: new BlogsData(),
    addition: new Addition<BlogT>(),
    edit: new Edit(),
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
