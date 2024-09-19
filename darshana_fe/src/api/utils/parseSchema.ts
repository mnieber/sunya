import { z } from 'zod';
import { convertDataToCamelCase } from '/src/api/utils/convertDataToCamelCase';
import { ObjT } from '/src/utils/types';

export const parseSchema = <SchemaT extends z.ZodType<any, any, any>>(
  schema: SchemaT,
  data: ObjT
) => {
  try {
    debugger;
    const transformedData = convertDataToCamelCase(schema, data);
    return schema.parse(transformedData);
  } catch (error) {
    console.error(error);
    return data;
  }
};
