import { Routes } from '@angular/router';

import { MainLayoutComponent } from './layout/main-layout/main-layout.component';

import { LoginComponent } from './pages/login/login.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { BooksComponent } from './pages/books/books.component';
import { MembersComponent } from './pages/members/members.component';
import { TransactionsComponent } from './pages/transactions/transactions.component';
import { IssueBookComponent } from './pages/issue-book/issue-book.component';
import { ReturnBookComponent } from './pages/return-book/return-book.component';

export const routes: Routes = [

  {
    path: '',
    component: MainLayoutComponent,
    children: [

      {
        path: '',
        redirectTo: 'dashboard',
        pathMatch: 'full'
      },

      {
        path: 'dashboard',
        component: DashboardComponent
      },

      {
        path: 'books',
        component: BooksComponent
      },

      {
        path: 'members',
        component: MembersComponent
      },

      {
        path: 'transactions',
        component: TransactionsComponent
      },

      {
        path: 'issue-book',
        component: IssueBookComponent
      },

      {
        path: 'return-book',
        component: ReturnBookComponent
      }

    ]
  },

  {
    path: 'login',
    component: LoginComponent
  }

];