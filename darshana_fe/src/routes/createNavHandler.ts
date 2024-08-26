import { DefaultProjectsNavHandler } from '/src/projects/routes';
import { NavHandler } from '/src/routes/navHandler';
import { DefaultScenariosNavHandler } from '/src/scenarios/routes';

export const createNavHandler = () => {
  const navHandler = new NavHandler();
  navHandler.installDefaultNavHandler(new DefaultProjectsNavHandler());
  navHandler.installDefaultNavHandler(new DefaultScenariosNavHandler());
  return navHandler;
};
