# Optional Example: Small App

Use this for a self-contained tool with multiple views. `MemoryRouter` is a good default because it keeps navigation inside the canvas.

```tsx
import React, { useMemo, useState } from "react";
import { MemoryRouter, NavLink, Route, Routes } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const seed = [
  { id: uuidv4(), title: "Ship the onboarding refresh", status: "In Review" },
  { id: uuidv4(), title: "Audit billing edge cases", status: "Planned" },
];

function Home() {
  return (
    <p className="text-sm text-slate-600">Choose a view from the sidebar.</p>
  );
}

function Workbench() {
  const [items, setItems] = useState(seed);
  const [draft, setDraft] = useState("");

  const total = useMemo(() => items.length, [items]);

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        <Input
          value={draft}
          onChange={(event) => setDraft(event.target.value)}
          placeholder="New task"
        />
        <Button
          onClick={() => {
            if (!draft.trim()) return;
            setItems((current) => [
              ...current,
              { id: uuidv4(), title: draft.trim(), status: "Draft" },
            ]);
            setDraft("");
          }}
        >
          Add
        </Button>
      </div>

      <Card>
        <CardHeader className="flex-row items-center justify-between space-y-0">
          <CardTitle>Tasks</CardTitle>
          <Badge variant="outline">{total} items</Badge>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Title</TableHead>
                <TableHead>Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {items.map((item) => (
                <TableRow key={item.id}>
                  <TableCell>{item.title}</TableCell>
                  <TableCell>{item.status}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}

export default function OpsWorkbench() {
  const linkClass = (active: boolean) =>
    [
      "rounded-lg px-3 py-2 text-sm font-medium transition",
      active ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-100",
    ].join(" ");

  return (
    <MemoryRouter initialEntries={["/"]}>
      <div className="min-h-screen bg-slate-100 p-6">
        <div className="mx-auto grid max-w-6xl gap-6 md:grid-cols-[220px_1fr]">
          <Card className="h-fit">
            <CardContent className="flex flex-col gap-2 p-3">
              <NavLink
                to="/"
                end
                className={({ isActive }) => linkClass(isActive)}
              >
                Overview
              </NavLink>
              <NavLink
                to="/workbench"
                className={({ isActive }) => linkClass(isActive)}
              >
                Workbench
              </NavLink>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-6">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/workbench" element={<Workbench />} />
              </Routes>
            </CardContent>
          </Card>
        </div>
      </div>
    </MemoryRouter>
  );
}
```
