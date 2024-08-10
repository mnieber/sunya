import * as Skandha from 'skandha';
import { Addition, Deletion, Edit, Highlight, Selection } from 'skandha-facets';
import { BlogPostT } from '/src/api/types';
import { registerBlogPostsCtr } from '/src/blogPosts/BlogPostsState/registerBlogPostsCtr';
import { BlogPostsData } from '/src/blogPosts/facets/BlogPostsData';
import { ObjT } from '/src/utils/types';

export type PropsT = {
  getBlogPosts: () => BlogPostT[];
  deleteBlogPosts: (ids: string[]) => Promise<any>;
  saveBlogPost: (values: ObjT) => Promise<any>;
  markBlogPostAsPublished: (blogPostId: string) => Promise<any>;
};

export class BlogPostsState {
  props: PropsT;

  blogPostsCtr = {
    data: new BlogPostsData(),
    addition: new Addition(),
    deletion: new Deletion(),
    edit: new Edit(),
    highlight: new Highlight<BlogPostT>(),
    selection: new Selection<BlogPostT>(),
  };

  actions = {
    markBlogPostAsPublished: (blogPostId: string) => {
      return this.props.markBlogPostAsPublished(blogPostId);
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerBlogPostsCtr(this);
  }
}
