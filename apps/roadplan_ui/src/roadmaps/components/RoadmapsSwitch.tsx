import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Route, Switch } from 'wouter';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { framesRoutes } from '/src/frames/routes';
import { ext } from '/src/routes/navHandler';

type PropsT = {};

const ContextProps = {
  blogsHighlight: blogsCtx.blogsHighlight,
};

export const BlogsSwitch = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <Switch>
        <Route path={ext(framesRoutes.dashboard())}>
        </Route>
      </Switch>
    );
  }, ContextProps)
);
