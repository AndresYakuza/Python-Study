import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', loadComponent: () => import('./products/list/list.component').then(m => m.ListComponent) },
  { path: '**', redirectTo: '' }
];

