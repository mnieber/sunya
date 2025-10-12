import { data, stub } from 'skandha';
import { AtlasT } from '/src/api/types';

export class AtlasData {
  static className = () => 'AtlasData';

  @data atlas: AtlasT | null = null;
  @data filteredAtlas: AtlasT | null = stub;
}
