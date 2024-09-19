import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { CardS } from '/src/frames/components/Card';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  reconstructedActorByKey: stepTreeCtx.reconstructedActorByKey,
  actorKey: stepTreeCtx.actorKey,
};

export const ActorView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const reconstructedActor = props.reconstructedActorByKey[props.actorKey];
    if (!reconstructedActor) {
      return null;
    }

    return (
      <div
        className={cn(
          'ActorView',
          CardS.padding.medium(),
          CardS.colours.default(),
          props.className
        )}
      >
        <h3 className="mb-2 text-xl font-bold text-blue-300">
          {reconstructedActor.key}
        </h3>
        <ul>
          {Object.entries(reconstructedActor.fields).map(([key, value]) => (
            <li key={key} className="text-gray-300">
              <span
                className={cn({
                  'font-bold': reconstructedActor.changedFields.includes(key),
                })}
              >
                <strong>{key}:</strong> {value.toString()}
              </span>
              {reconstructedActor.changedFields.includes(key) && (
                <span className="ml-2 text-green-400">(Changed)</span>
              )}
            </li>
          ))}
        </ul>
      </div>
    );
  }, ContextProps)
);
