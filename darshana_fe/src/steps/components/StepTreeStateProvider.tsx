import { observer } from 'mobx-react-lite';
import React from 'react';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { StepTreeContext } from '/src/steps/hooks/useStepTreeContext';
import { useStepTreeState } from '/src/steps/hooks/useStepTreeState';

type PropsT = React.PropsWithChildren<{
  scenario: ScenarioT;
}>;

export const StepTreeStateProvider = observer((props: PropsT) => {
  const { stepTreeState } = useStepTreeState({
    getScenario: () => props.scenario,
  });

  const value = React.useMemo(
    () => ({
      stepTreeState,
      rootStep: stepTreeState.props.getRootStep(),
      reconstructedActor: stepTreeState.stepTreeCtr.data.reconstructedActor,
    }),
    [stepTreeState]
  );

  return (
    <StepTreeContext.Provider value={value}>
      {props.children}
    </StepTreeContext.Provider>
  );
});
