# Optional Example: UI-Heavy Prototype

Use this for a dense interface concept with overlays, filters, side panels, and staged interactions.

```tsx
import React from "react";
import {
  IconBellDot as Bell,
  IconCommand as Command,
  IconLayers3 as Layers3,
  IconSparkle as Sparkles,
} from "nucleo-sharp";

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

export default function CreativeControlRoom() {
  return (
    <div className="min-h-screen bg-[linear-gradient(135deg,#10131c,#1f2937,#111827)] p-6 text-white">
      <div className="mx-auto max-w-7xl space-y-6">
        <div className="flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/10 p-4 backdrop-blur md:flex-row md:items-center md:justify-between">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-orange-500/20 p-3 text-orange-200">
              <Sparkles className="h-5 w-5" />
            </div>
            <div>
              <h1 className="text-2xl font-semibold">Creative Control Room</h1>
              <p className="text-sm text-white/60">
                Prototype for a studio command center
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="outline">
                  <Bell className="mr-2 h-4 w-4" />
                  Alerts
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent>
                <DropdownMenuItem>Render queue slowed down</DropdownMenuItem>
                <DropdownMenuItem>New review requested</DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>

            <Sheet>
              <SheetTrigger asChild>
                <Button>
                  <Layers3 className="mr-2 h-4 w-4" />
                  Open side panel
                </Button>
              </SheetTrigger>
              <SheetContent className="bg-slate-950 text-white">
                <SheetHeader>
                  <SheetTitle>Studio Notes</SheetTitle>
                </SheetHeader>
                <div className="mt-6 space-y-3 text-sm text-white/70">
                  <p>
                    Use sheets for inspector panels, settings, or compact
                    workflows.
                  </p>
                  <p>
                    Use dialogs when the interaction should fully interrupt the
                    flow.
                  </p>
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>

        <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
          <Card className="border-white/10 bg-white/10 text-white">
            <CardHeader>
              <CardTitle>Workspace</CardTitle>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="timeline" className="space-y-4">
                <TabsList className="bg-white/10">
                  <TabsTrigger value="timeline">Timeline</TabsTrigger>
                  <TabsTrigger value="layers">Layers</TabsTrigger>
                  <TabsTrigger value="assets">Assets</TabsTrigger>
                </TabsList>
                <TabsContent
                  value="timeline"
                  className="rounded-2xl border border-white/10 p-4"
                >
                  <div className="grid gap-3 md:grid-cols-3">
                    {["Research", "Draft", "Review"].map((stage) => (
                      <div key={stage} className="rounded-xl bg-black/20 p-4">
                        <div className="mb-2 flex items-center justify-between">
                          <span className="font-medium">{stage}</span>
                          <Badge className="bg-white/10 text-white">3</Badge>
                        </div>
                        <div className="text-sm text-white/60">
                          Stage preview content
                        </div>
                      </div>
                    ))}
                  </div>
                </TabsContent>
                <TabsContent
                  value="layers"
                  className="rounded-2xl border border-white/10 p-4"
                >
                  <p className="text-sm text-white/70">
                    Use tabs for alternate working surfaces.
                  </p>
                </TabsContent>
                <TabsContent
                  value="assets"
                  className="rounded-2xl border border-white/10 p-4"
                >
                  <p className="text-sm text-white/70">
                    Dense prototypes can stay self-contained inside one file.
                  </p>
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>

          <Card className="border-white/10 bg-white/10 text-white">
            <CardHeader className="flex-row items-center justify-between space-y-0">
              <CardTitle>Activity</CardTitle>
              <Avatar>
                <AvatarFallback>GV</AvatarFallback>
              </Avatar>
            </CardHeader>
            <CardContent>
              <ScrollArea className="h-80 pr-4">
                <Accordion type="single" collapsible className="w-full">
                  <AccordionItem value="a">
                    <AccordionTrigger>Assistant actions</AccordionTrigger>
                    <AccordionContent>
                      Use accordions to compress dense operational detail.
                    </AccordionContent>
                  </AccordionItem>
                  <AccordionItem value="b">
                    <AccordionTrigger>Command palette ideas</AccordionTrigger>
                    <AccordionContent>
                      <div className="flex items-center gap-2 text-sm text-white/70">
                        <Command className="h-4 w-4" />
                        Pair command-style layouts with lists, badges, and
                        dialogs.
                      </div>
                    </AccordionContent>
                  </AccordionItem>
                </Accordion>
              </ScrollArea>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
```
