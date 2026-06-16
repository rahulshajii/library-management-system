import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TransactionService } from '../../services/transaction.service';

@Component({
  selector: 'app-transactions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './transactions.component.html',
  styleUrl: './transactions.component.css'
})
export class TransactionsComponent implements OnInit {

  transactions: any[] = [];

  constructor(private transactionService: TransactionService) {}

  ngOnInit(): void {

    this.transactionService.getTransactions().subscribe({

      next: (data) => {
        this.transactions = data;
      },

      error: (err) => {
        console.log(err);
      }

    });

  }

}
