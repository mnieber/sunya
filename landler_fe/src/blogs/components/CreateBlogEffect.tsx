import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { BlogT, createBlog } from '/src/api/types/BlogT';
import { authStateCtx } from '/src/auth/hooks/useAuthStateContext';
import { authNav } from '/src/auth/routes';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';
import { navTo } from '/src/routes/navHandler';

type PropsT = {};

const ContextProps = {
  blogsAddition: blogsCtx.blogsAddition,
  authState: authStateCtx.authState,
};

export const CreateBlogEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { hasUrlChanged } = useRefUrl();
    const { blogsAddition } = props;

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (!props.authState.isAuthenticated) {
          navTo(authNav.signIn({}));
        }
        if (!blogsAddition.item) {
          const values: BlogT = createBlog({});
          blogsAddition.add({ values });
        }
      }
    });

    return null;
  }, ContextProps)
);
