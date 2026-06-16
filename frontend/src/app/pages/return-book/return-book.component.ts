import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { TransactionService } from '../../services/transaction.service';

@Component({
  selector: 'app-return-book',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './return-book.component.html',
  styleUrl: './return-book.component.css'
})
export class ReturnBookComponent implements OnInit {

  transactions: any[] = [];

  selectedTransaction = '';

  constructor(private transactionService: TransactionService) {}

  ngOnInit(): void {

    this.transactionService.getTransactions().subscribe(data => {

      this.transactions = data.filter(
        (t: any) => t.status === 'ISSUED'
      );

    });

  }

returnBook() {

  this.transactionService
      .returnBook(Number(this.selectedTransaction))
      .subscribe({

        next: () => {

          alert('Book Returned Successfully');

          window.location.reload();

        },

        error: (err) => {

          console.log(err);

          alert('Failed to Return Book');

        }

      });

}



}
