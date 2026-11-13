# Optional Example: Form And Workflow

Use this for setup flows, editors, request forms, onboarding, and approval screens.

```tsx
import React, { useMemo, useState } from "react";

import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Progress } from "@/components/ui/progress";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";

export default function LaunchForm() {
  const [step, setStep] = useState(1);
  const [name, setName] = useState("");
  const [team, setTeam] = useState("product");
  const [notes, setNotes] = useState("");
  const [notify, setNotify] = useState(true);
  const [agreed, setAgreed] = useState(false);

  const progress = useMemo(() => (step / 3) * 100, [step]);

  return (
    <div className="min-h-screen bg-stone-100 p-6">
      <div className="mx-auto max-w-2xl rounded-3xl border bg-white p-6 shadow-sm">
        <div className="mb-6 space-y-3">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-semibold">Launch Checklist</h1>
            <span className="text-sm text-stone-500">Step {step} / 3</span>
          </div>
          <Progress value={progress} />
        </div>

        <div className="space-y-5">
          <div className="space-y-2">
            <Label>Project name</Label>
            <Input
              value={name}
              onChange={(event) => setName(event.target.value)}
            />
          </div>

          <div className="space-y-2">
            <Label>Owning team</Label>
            <Select value={team} onValueChange={setTeam}>
              <SelectTrigger>
                <SelectValue placeholder="Pick a team" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="product">Product</SelectItem>
                <SelectItem value="design">Design</SelectItem>
                <SelectItem value="operations">Operations</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <Label>Rollout notes</Label>
            <Textarea
              rows={5}
              value={notes}
              onChange={(event) => setNotes(event.target.value)}
            />
          </div>

          <div className="flex items-center justify-between rounded-xl border p-4">
            <div>
              <div className="font-medium">Notify stakeholders</div>
              <div className="text-sm text-stone-500">
                Send updates when the launch status changes.
              </div>
            </div>
            <Switch checked={notify} onCheckedChange={setNotify} />
          </div>

          <label className="flex items-center gap-3 rounded-xl border p-4">
            <Checkbox
              checked={agreed}
              onCheckedChange={(value) => setAgreed(Boolean(value))}
            />
            <span className="text-sm">
              I reviewed the launch plan and the rollback instructions.
            </span>
          </label>
        </div>

        <div className="mt-6 flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => setStep((current) => Math.max(1, current - 1))}
          >
            Previous
          </Button>

          <Dialog>
            <DialogTrigger asChild>
              <Button
                onClick={() => setStep((current) => Math.min(3, current + 1))}
                disabled={!name || !agreed}
              >
                Review submission
              </Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Ready to launch</DialogTitle>
                <DialogDescription>
                  {name} will be routed to the {team} team with notifications{" "}
                  {notify ? "enabled" : "disabled"}.
                </DialogDescription>
              </DialogHeader>
            </DialogContent>
          </Dialog>
        </div>
      </div>
    </div>
  );
}
```
