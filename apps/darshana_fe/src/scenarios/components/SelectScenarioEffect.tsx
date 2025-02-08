import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { useParams } from 'wouter';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';
import { UrlEffectView } from '/src/utils/components';
import { ObjT } from '/src/utils/types';

type PropsT = {};

const ContextProps = {
  scenarios: projectCtx.scenarios,
  scenario: projectCtx.scenario,
  scenariosHighlight: projectCtx.scenariosHighlight,
};

export const SelectScenarioEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const params = useParams() as ObjT;
    const { updateRefUrl, hasUrlChanged } = useRefUrl();

    const { scenariosHighlight, scenario, scenarios } = props;
    const scenarioFromUrl = R.find(
      (x: ScenarioT) => x.id === params.scenarioId
    )(scenarios);
    const isScenarioInSyncWithUrl = scenario?.id === scenarioFromUrl?.id;

    const selectScenario = (scenario?: ScenarioT) => {
      scenariosHighlight.set({ itemId: scenario?.id });
    };

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (scenarioFromUrl) {
          updateRefUrl();
          if (!isScenarioInSyncWithUrl) {
            selectScenario(scenarioFromUrl);
          }
        } else {
          selectScenario(undefined);
        }
      }
    });

    return (
      <UrlEffectView
        resourceName="scenario"
        isInSync={isScenarioInSyncWithUrl}
        className="absolute"
      />
    );
  }, ContextProps)
);
