import * as Skandha from 'skandha';
import { Deletion, Filtering, Highlight, Selection } from 'skandha-facets';
import { BlogPostT } from '/src/api/types';
import { registerBlogPostsCtr } from '/src/blogPosts/BlogPostsState/registerBlogPostsCtr';
import { BlogPostsData } from '/src/blogPosts/facets/BlogPostsData';

export type PropsT = {
  getBlogPosts: () => BlogPostT[];
  deleteBlogPosts: (ids: string[]) => Promise<any>;
};

export class BlogPostsState {
  props: PropsT;

  blogPostsCtr = {
    data: new BlogPostsData(),
    deletion: new Deletion(),
    filtering: new Filtering(),
    highlight: new Highlight<BlogPostT>(),
    selection: new Selection<BlogPostT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerBlogPostsCtr(this);
  }
}
