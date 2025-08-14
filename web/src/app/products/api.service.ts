import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Item { id: number; name: string; }

@Injectable({ providedIn: 'root' })
export class ApiService {
  private http = inject(HttpClient);
  getItems(): Observable<Item[]> { return this.http.get<Item[]>('/items'); }
  createItem(name: string): Observable<Item> { return this.http.post<Item>('/items', { name }); }
  updateItem(id: number, name: string): Observable<Item> { return this.http.put<Item>(`/items/${id}`, { name }); }
  deleteItem(id: number): Observable<Item> { return this.http.delete<Item>(`/items/${id}`); }
}
