import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActorView } from '/src/actors/components/ActorView';
import { L } from '/src/frames/layout';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  reconstructedActorByKey: stepTreeCtx.reconstructedActorByKey,
  actorContext: stepTreeCtx.actorContext,
};

export const ActorContextView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.actorContext) {
      return null;
    }

    return (
      <div className={cn('ActorContextView', L.row.skewer(), props.className)}>
        <ActorView
          actor={props.reconstructedActorByKey[props.actorContext.actorKey]}
        />
        {!!props.actorContext.otherActorKey && (
          <ActorView
            actor={
              props.reconstructedActorByKey[props.actorContext.otherActorKey]
            }
          />
        )}
      </div>
    );
  }, ContextProps)
);
