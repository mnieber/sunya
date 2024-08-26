import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  reconstructedActor: stepTreeCtx.reconstructedActor,
};

export const ActorView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.reconstructedActor) {
      return null;
    }

    return (
      <div
        className={cn(
          'ActorView',
          'rounded-lg bg-gray-800 p-4',
          props.className
        )}
      >
        <h3 className="mb-2 text-xl font-bold text-white">
          Actor: {props.reconstructedActor.key}
        </h3>
        <p className="text-gray-300">
          <strong>ID:</strong> {props.reconstructedActor.id}
        </p>
        <h4 className="mb-2 mt-4 text-lg font-semibold text-white">Fields:</h4>
        <ul className="space-y-1">
          {Object.entries(props.reconstructedActor.fields).map(
            ([key, value]) => (
              <li key={key} className="text-gray-300">
                <span
                  className={cn({
                    'font-bold':
                      props.reconstructedActor.changed_fields.includes(key),
                  })}
                >
                  <strong>{key}:</strong> {value.toString()}
                </span>
                {props.reconstructedActor.changed_fields.includes(key) && (
                  <span className="text-green-400 ml-2">(Changed)</span>
                )}
              </li>
            )
          )}
        </ul>
      </div>
    );
  }, ContextProps)
);
