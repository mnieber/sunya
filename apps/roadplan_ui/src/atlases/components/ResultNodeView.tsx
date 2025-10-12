import { observer } from 'mobx-react-lite';
import { ResultT } from '/src/api/types';
import { cn } from '/src/utils/classnames';

import './ResultNodeView.scss';

export type PropsT = {
  result: ResultT;
  selectItem: Function;
  highlightItem: Function;
  isSelected: boolean;
  isZoomedResult?: boolean;
  hideCheckbox?: boolean;
  roadmapOwner?: string;
  className?: any;
};

export const ResultNodeView = observer((props: PropsT) => {
  const displayOwner = props.result.owner || props.roadmapOwner;
  const isOwnerFallback = !props.result.owner && !!props.roadmapOwner;

  return (
    <div
      className={cn(
        'ResultNodeView',
        'flex items-center gap-3',
        props.className,
        {
          'ResultNodeView--zoomed': props.isZoomedResult,
        }
      )}
    >
      {!props.hideCheckbox && (
        <input
          type="checkbox"
          checked={props.isSelected}
          readOnly
          className="ResultNodeView__checkbox"
          onClick={(e) => {
            e.stopPropagation();
            props.selectItem({ itemId: props.result.id, isCtrl: true });
          }}
        />
      )}
      <span
        className="ResultNodeView__label"
        onClick={(e) => {
          props.highlightItem({ itemId: props.result.id });
        }}
      >
        {props.result.name}
      </span>
      {displayOwner && (
        <span
          className={cn('ResultNodeView__owner', {
            'ResultNodeView__owner--fallback': isOwnerFallback,
          })}
        >
          {displayOwner}
        </span>
      )}
    </div>
  );
});
