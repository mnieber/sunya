import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { blogsNav } from '/src/blogs/routes';
import { DialogButton } from '/src/frames/components/DialogButton/DialogButton';
import { navStateCtx } from '/src/routes/hooks/useNavStateContext';
import { navTo } from '/src/routes/navHandler';
import { cn } from '/src/utils/classnames';

// Import styles
import './CreateBlogButton.scss';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  navState: navStateCtx.navState,
};

export const CreateBlogButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <DialogButton
        className={cn('CreateBlogButton', props.className)}
        onClick={() => {
          props.navState.storeNavPoint();
          navTo(blogsNav.createBlog({}));
        }}
        label="Create blog"
      />
    );
  }, ContextProps)
);
