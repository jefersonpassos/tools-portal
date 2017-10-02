import { Injectable } from '@angular/core';

import { Tools } from './tools.model';
import { TOOLS } from './mock-tools';

@Injectable()
export class ToolsService {

  constructor() { }

  getTools(): Tools[] {
    return TOOLS;
  };

}
