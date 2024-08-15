import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import { withContextProps } from 'react-props-from-context';
import { Selection, SelectionUIConnector } from 'skandha-facets';
import { EntityT } from '/src/api/types/EntityT';
import { EntityListViewKeyHandler } from '/src/entities/components';
import { EntityListViewItem } from '/src/entities/components/EntityListViewItem';
import { entitiesCtx } from '/src/entities/hooks/useEntitiesContext';
import { LoaderBar } from '/src/frames/components/LoaderBar';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './EntityListView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  entities: entitiesCtx.entities,
  entitiesHighlight: entitiesCtx.entitiesHighlight,
  entitiesSelection: entitiesCtx.entitiesSelection,
};

export const EntityListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    //
    // 🔳  Handle loading state 🔳
    //
    if (isLoading(props.entities)) {
      return <EntityListViewLoader {...props} />;
    }

    const selectionUIConnector = new SelectionUIConnector({
      selection: props.entitiesSelection as Selection<EntityT>,
      onSelect: (args: {
        itemId: string | undefined;
        isShift?: boolean | undefined;
        isCtrl?: boolean | undefined;
      }) => {
        if (!args.isShift && !args.isCtrl) {
          const entity = props.entities.find((x) => x.id === args.itemId);
          if (entity) {
            // MOONLEAP TODO: navigate to entity
          }
        }
      },
    });

    //
    // 🔳 entityDivs 🔳
    //
    const entityDivs = props.entities.map((entity) => {
      return (
        <EntityListViewItem
          key={`item-${entity.id}`}
          entity={entity}
          isHighlighted={entity && props.entitiesHighlight.itemId === entity.id}
          selectionUIProps={selectionUIConnector.handle(entity.id)}
        />
      );
    });

    const noItems = <div>There are no entities</div>;

    //
    // 🔳 EntityListView 🔳
    //
    return (
      <EntityListViewKeyHandler>
        <div
          className={cn('EntityListView', [L.col.banner(), props.className])}
          tabIndex={0}
        >
          {entityDivs.length > 0 && entityDivs}
          {entityDivs.length === 0 && noItems}
        </div>
      </EntityListViewKeyHandler>
    );
  }, ContextProps)
);

export const EntityListViewLoader = (props: { className?: any }) => {
  const loaderBars = ['1', '2', '3'].map((id: string) => {
    return <LoaderBar key={`item-${id}`} className={cn('my-4 h-6')} />;
  });

  return (
    <div
      className={cn('EntityListViewLoader', [L.col.banner(), props.className])}
    >
      {loaderBars}
    </div>
  );
};
