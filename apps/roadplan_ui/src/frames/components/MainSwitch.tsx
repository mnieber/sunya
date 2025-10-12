import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Route, Switch } from 'wouter';
import { framesRoutes } from '/src/frames/routes';
import { ext } from '/src/routes/navHandler';
import {
  AtlasBriefsListView,
  AtlasView,
  SelectAtlasBriefEffect,
} from '/src/atlases/components';
import { atlasesRoutes } from '/src/atlases/routes';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';

type PropsT = {};

const ContextProps = {
  roadmapsHighlight: atlasCtx.roadmapsHighlight,
};

export const MainSwitch = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <Switch>
        <Route path={ext(framesRoutes.dashboard())}>
          <Route path={framesRoutes.dashboard()}>
            <AtlasBriefsListView />
          </Route>
          <Route path={ext(atlasesRoutes.atlas())}>
            <SelectAtlasBriefEffect />
            <AtlasView />
          </Route>
        </Route>
      </Switch>
    );
  }, ContextProps)
);
