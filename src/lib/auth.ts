// Simple auth store
import { writable } from 'svelte/store';

export const isAuthenticated = writable(false);

const ADMIN_CREDENTIALS = {
  email: 'admin@scriptive.ai',
  password: 'admin123'
};

export function login(email: string, password: string): boolean {
  if (email === ADMIN_CREDENTIALS.email && password === ADMIN_CREDENTIALS.password) {
    isAuthenticated.set(true);
    return true;
  }
  return false;
}

export function logout() {
  isAuthenticated.set(false);
}