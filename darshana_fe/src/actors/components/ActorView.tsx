import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActorT } from '/src/api/types/ActorT';
import { CardS } from '/src/frames/components/Card';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
  actor: ActorT | null;
};

const ContextProps = {};

export const ActorView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.actor) {
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
          {props.actor.key}
        </h3>
        <ul>
          {Object.entries(props.actor.fields).map(([key, value]) => (
            <li key={key} className="text-gray-300">
              <span
                className={cn({
                  'font-bold': props.actor!.changedFields.includes(key),
                })}
              >
                <strong>{key}:</strong> {value.toString()}
              </span>
              {props.actor!.changedFields.includes(key) && (
                <span className="ml-2 text-green-400">(Changed)</span>
              )}
            </li>
          ))}
        </ul>
      </div>
    );
  }, ContextProps)
);
