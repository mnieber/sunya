/*
The BlogPostsState class has a blogPostsCtr container with a data facet (that contains the blogPosts)
and deletion, filtering, highlight and selection facets (these are reusable behaviours).

The BlogPostsState class has properties that connect the state to the outside world (e.g. getBlogPosts).

The registerBlogPostsCtr function registers the blogPostsCtr container with the BlogPostsState. When the
blogPostsCtr is registered, it can bind to the properties of the BlogPostsState (e.g. this allows the
blogPostsCtr.deletion facet to call the deleteBlogPosts property of the BlogPostsState).

You can continue by:

- reading the registerBlogPostsCtr.ts file.
*/

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
