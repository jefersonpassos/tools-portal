import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';

import { Tools } from './tools';
import { TOOLS } from './mock-tools';

@Injectable()
export class ToolsService {

  apiUrl = environment.apiUrl;

  constructor(private http:HttpClient) { }

  getTools(){
      return this.http.get<Tools[]>(this.apiUrl + '/tools/');
  }

  ngOnInit() {

  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
