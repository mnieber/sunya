import { observer } from 'mobx-react-lite';
import { ResultT } from '/src/api/types';
import { cn } from '/src/utils/classnames';
import { Icon } from '/src/frames/components';

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

const truncateOwner = (owner: string): string => {
  if (owner.length <= 13) {
    return owner;
  }
  return owner.substring(0, 10) + '...';
};

export const ResultNodeView = observer((props: PropsT) => {
  const displayOwner = props.result.owner || props.roadmapOwner;
  const isOwnerFallback = !props.result.owner && !!props.roadmapOwner;
  const truncatedOwner = displayOwner ? truncateOwner(displayOwner) : '';
  const prefix = props.result.resultType == 'ms' ? 'ms/' : '';
  const postfix = props.result.isDone ? ' ✅' : '';

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
        {prefix + props.result.name + postfix}
      </span>
      <div className="ResultNodeView__columns">
        {props.result.jiraTicketUrls.length > 0 && (
          <div className="ResultNodeView__jira-tickets">
            {props.result.jiraTicketUrls.map((url, index) => (
              <a
                key={index}
                href={url}
                target="_blank"
                rel="noopener noreferrer"
                className="ResultNodeView__jira-link"
                onClick={(e) => e.stopPropagation()}
              >
                <Icon
                  name="externalLink"
                  className="ResultNodeView__jira-icon"
                />
              </a>
            ))}
          </div>
        )}
        {truncatedOwner && (
          <span
            className={cn('ResultNodeView__owner', {
              'ResultNodeView__owner--fallback': isOwnerFallback,
            })}
          >
            {truncatedOwner}
          </span>
        )}
        <span
          className={cn('ResultNodeView__result-type', {
            'ResultNodeView__result-type--bug': props.result.resultType === 'bug',
          })}
        >
          {props.result.resultType}
        </span>
        <span className="ResultNodeView__is-done">
          {props.result.isDone ? '✓' : ''}
        </span>
      </div>
    </div>
  );
});
