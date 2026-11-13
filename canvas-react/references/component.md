# Optional Example: Component

Use this for a focused, interactive component rather than a full app shell.

```tsx
import React, { useState } from "react";
import { motion } from "framer-motion";
import { IconBolt as Zap, IconSparkle as Sparkles } from "nucleo-sharp";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Switch } from "@/components/ui/switch";

export default function ThemeConfigurator() {
  const [enabled, setEnabled] = useState(true);

  return (
    <div className="flex min-h-screen items-center justify-center bg-[linear-gradient(135deg,#020617,#0f172a,#431407)] p-8 text-white">
      <motion.div
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.35 }}
        className="w-full max-w-md"
      >
        <Card className="border-white/10 bg-white/10 backdrop-blur">
          <CardHeader className="space-y-3">
            <div className="flex items-center justify-between">
              <Badge className="gap-2 bg-orange-500/20 text-orange-200">
                <Sparkles className="h-3.5 w-3.5" />
                Live Preview
              </Badge>
              <Switch checked={enabled} onCheckedChange={setEnabled} />
            </div>
            <CardTitle className="text-white">Theme Configurator</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="rounded-xl border border-white/10 bg-black/20 p-4">
              <div className="mb-2 flex items-center gap-2 text-sm text-white/70">
                <Zap className="h-4 w-4 text-orange-300" />
                Accent intensity
              </div>
              <div className="h-3 overflow-hidden rounded-full bg-white/10">
                <motion.div
                  animate={{ width: enabled ? "78%" : "22%" }}
                  className="h-full rounded-full bg-linear-to-r from-orange-400 to-pink-500"
                />
              </div>
            </div>

            <Button className="w-full">
              {enabled ? "Apply dynamic theme" : "Use subtle theme"}
            </Button>
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}
```
