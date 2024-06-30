import { observer } from 'mobx-react-lite';
import { selectionUIHandlers, SelectionUIPropsT } from 'skandha-facets';
import { EntityT } from '/src/api/types/EntityT';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './EntityListViewItem.scss';

export type PropsT = {
  entity: EntityT;
  isHighlighted: boolean;
  selectionUIProps: SelectionUIPropsT;
  className?: any;
};

export const EntityListViewItem = observer((props: PropsT) => {
  return (
    /*
      🔳 EntityListViewItem 🔳
      */
    <div
      className={cn(
        [
          'EntityListViewItem',
          {
            'EntityListViewItem--selected': props.selectionUIProps.isSelected,
            'EntityListViewItem--highlighted': props.isHighlighted,
          },
        ],
        [props.className]
      )}
      {...selectionUIHandlers(props.selectionUIProps)}
    >
      {
        // 🔳 Body 🔳
      }
      <div className={cn('EntityListViewItem__Body', [L.row.skewer()])}>
        Entity
      </div>
    </div>
  );
});
