import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { BlogT, createBlog } from '/src/api/types/BlogT';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';

type PropsT = {};

const ContextProps = {
  blogs: blogsCtx.blogs,
  blog: blogsCtx.blog,
  blogsAddition: blogsCtx.blogsAddition,
};

export const CreateBlogEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { hasUrlChanged } = useRefUrl();
    const { blogsAddition } = props;

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (!blogsAddition.item) {
          const values: BlogT = createBlog({});
          blogsAddition.add({ values });
        }
      }
    });

    return null;
  }, ContextProps)
);
