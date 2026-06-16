import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { BookService } from '../../services/book.service';
import { MemberService } from '../../services/member.service';

@Component({
  selector: 'app-issue-book',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './issue-book.component.html',
  styleUrl: './issue-book.component.css'
})
export class IssueBookComponent implements OnInit {

  books: any[] = [];
  members: any[] = [];

  selectedBook = '';
  selectedMember = '';
  dueDate = '';

  constructor(
    private bookService: BookService,
    private memberService: MemberService
  ) {}

  ngOnInit(): void {

    this.bookService.getBooks().subscribe(data => {
      this.books = data;
    });

    this.memberService.getMembers().subscribe(data => {
      this.members = data;
    });

  }
issueBook() {

  const transaction = {

    member: Number(this.selectedMember),
    book: Number(this.selectedBook),
    due_date: this.dueDate,
    status: 'ISSUED'

  };

  this.bookService.issueBook(transaction).subscribe({

    next: () => {

      alert('Book Issued Successfully!');

      window.location.reload();

    },

    error: (err) => {

      console.log(err);

      alert('Failed to Issue Book');

    }

  });

}

}
