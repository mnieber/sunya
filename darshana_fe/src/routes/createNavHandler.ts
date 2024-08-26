import { DefaultProjectsNavHandler } from '/src/projects/routes';
import { NavHandler } from '/src/routes/navHandler';

export const createNavHandler = () => {
  const navHandler = new NavHandler();
  navHandler.installDefaultNavHandler(new DefaultProjectsNavHandler());
  return navHandler;
};
