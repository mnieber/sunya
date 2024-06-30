import { observer } from 'mobx-react-lite';
import { isUpdating } from 'mobx-resource-states';
import { highlightUIHandlers, HighlightUIPropsT } from 'skandha-facets';
import { StepT } from '/src/api/types/StepT';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './StepListViewItem.scss';

export type PropsT = {
  step: StepT;
  highlightUIProps: HighlightUIPropsT;
  className?: any;
};

export const StepListViewItem = observer((props: PropsT) => {
  return (
    /*
      🔳 StepListViewItem 🔳
      */
    <div
      className={cn(
        [
          'StepListViewItem',
          {
            'StepListViewItem--highlighted':
              props.highlightUIProps.isHighlighted,
            'animate-delete': isUpdating(props.step),
          },
        ],
        [props.className]
      )}
      {...highlightUIHandlers(props.highlightUIProps)}
    >
      {
        // 🔳 Body 🔳
      }
      <div className={cn('StepListViewItem__Body', [L.row.skewer()])}>Step</div>
    </div>
  );
});
