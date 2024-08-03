import { observer } from 'mobx-react-lite';
import { isUpdating } from 'mobx-resource-states';
import { withContextProps } from 'react-props-from-context';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
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
      <ActionButton
        disabled={disabled}
        danger={true}
        className={cn('DeleteBlogPostsButton', props.className)}
        onClick={() =>
          props.blogPostsDeletion.delete({
            itemIds: props.blogPostsSelection.itemIds,
          })
        }
        label="Delete selected blog posts"
      />
    );
  }, ContextProps)
);
