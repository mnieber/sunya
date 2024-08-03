import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { blogsNav } from '/src/blogs/routes';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
import { navTo } from '/src/routes/navHandler';
import { cn } from '/src/utils/classnames';

// Import styles
import './CreateBlogButton.scss';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  blog: blogsCtx.blog,
  blogsAddition: blogsCtx.blogsAddition,
};

export const CreateBlogButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <ActionButton
        className={cn('CreateBlogButton', props.className)}
        onClick={() => navTo(blogsNav.createBlog({}))}
        label="Create blog"
      />
    );
  }, ContextProps)
);
