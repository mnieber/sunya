import { DeletionWithFlag } from 'skandha-facets';
import { BlogPostT } from '/src/api/types';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';

export class BlogPostsDeletion extends DeletionWithFlag<BlogPostT> {
  constructor(private state: BlogPostsState) {
    super();
  }

  protected deleteItems(args: { itemIds: string[]; moveToTrash?: boolean }): any {
    return this.state.props.deleteBlogPosts(args.itemIds);
  }
}
