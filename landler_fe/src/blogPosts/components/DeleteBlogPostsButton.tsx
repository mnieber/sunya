/*
Just like BlogPostsFilter, the DeleteBlogPostsButton is quite simple. It calls the delete method of
blogPostsDeletion, passing the ids of the selected blogPosts.
*/

import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import { isUpdating } from '/src/resourceStates/getState';
import { cn } from '/src/utils/classnames';

// Import styles
import './DeleteBlogPostsButton.scss';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  blogPosts: blogPostsCtx.blogPosts,
  blogPostsDeletion: blogPostsCtx.blogPostsDeletion,
  blogPostsSelection: blogPostsCtx.blogPostsSelection,
};

export const DeleteBlogPostsButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const disabled =
      props.blogPostsSelection.itemIds.length === 0 ||
      isUpdating(props.blogPosts);

    return (
      <button
        disabled={disabled}
        className={cn(
          'DeleteBlogPostsButton',
          'my-4',
          {
            'DeleteBlogPostsButton--enabled': !disabled,
            'DeleteBlogPostsButton--disabled': disabled,
          },
          props.className
        )}
        onClick={() =>
          props.blogPostsDeletion.delete({
            itemIds: props.blogPostsSelection.itemIds,
          })
        }
      >
        Delete selected blogPosts
      </button>
    );
  }, ContextProps)
);
