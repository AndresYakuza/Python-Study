import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { ApiService, Item } from '../api.service';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent {
  api = inject(ApiService);
  fb = inject(FormBuilder);

  items = signal<Item[]>([]);
  editingId = signal<number | null>(null);
  error = signal<string | null>(null);

  f = this.fb.group({ name: ['', [Validators.required, Validators.minLength(2)]] });

  ngOnInit() { this.load(); }

  load() {
    this.api.getItems().subscribe({
      next: v => this.items.set(v),
      error: () => this.error.set('No se pudo cargar la lista')
    });
  }

  save() {
    const name = this.f.value.name?.trim() || '';
    if (!name) return;
    const id = this.editingId();
    const obs = id ? this.api.updateItem(id, name) : this.api.createItem(name);
    obs.subscribe({
      next: () => { this.f.reset(); this.editingId.set(null); this.load(); },
      error: () => this.error.set('Error al guardar')
    });
  }

  edit(it: Item) {
    this.f.patchValue({ name: it.name });
    this.editingId.set(it.id);
  }

  cancel() {
    this.f.reset();
    this.editingId.set(null);
  }

  remove(it: Item) {
    this.api.deleteItem(it.id).subscribe({
      next: () => this.load(),
      error: () => this.error.set('Error al eliminar')
    });
  }

  trackById = (_: number, it: Item) => it.id;
}
