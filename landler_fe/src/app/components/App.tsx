import { QueryClientProvider } from '@tanstack/react-query';
import * as R from 'ramda';
import { queryClient } from '/src/api/queryClient';
import { AuthStateProvider } from '/src/auth/components/AuthStateProvider';
import { AuthSwitch } from '/src/auth/components/AuthSwitch';
import { BlogPostsStateProvider } from '/src/blogPosts/components/BlogPostsStateProvider';
import { BlogsStateProvider } from '/src/blogs/components/BlogsStateProvider';
import { BlogsSwitch } from '/src/blogs/components/BlogsSwitch';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './App.scss';

export const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <AppBody>
        <AuthStateProvider>
          <AuthSwitch />
          <BlogsStateProvider>
            <BlogPostsStateProvider>
              <BlogsSwitch />
            </BlogPostsStateProvider>
          </BlogsStateProvider>
        </AuthStateProvider>
      </AppBody>
    </QueryClientProvider>
  );
};

const AppBody = (props: React.PropsWithChildren<{}>) => {
  return (
    <div
      id="App"
      className={cn('App', [
        R.values({
          root: L.col.banner(),
          // 320px = breakpoints.xs
          size: `min-width-[320px] h-screen`,
          scroll: 'overflow-x-hidden',
        }),
      ])}
      tabIndex={0}
      ref={(x: any) => x?.focus()}
    >
      {props.children}
    </div>
  );
};
