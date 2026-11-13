# Optional Example: Dashboard

Use this for analytics, KPIs, trend views, and filterable reporting. `recharts` works well with cards, tabs, badges, and selects.

```tsx
import React, { useMemo, useState } from "react";
import {
  IconArrowTrendUp as TrendingUp,
  IconArrowUpRight as ArrowUpRight,
} from "nucleo-sharp";
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const ranges = {
  "7d": [
    { label: "Mon", revenue: 18, tickets: 12 },
    { label: "Tue", revenue: 22, tickets: 16 },
    { label: "Wed", revenue: 20, tickets: 14 },
    { label: "Thu", revenue: 28, tickets: 20 },
    { label: "Fri", revenue: 32, tickets: 24 },
    { label: "Sat", revenue: 30, tickets: 18 },
    { label: "Sun", revenue: 35, tickets: 26 },
  ],
  "30d": [
    { label: "W1", revenue: 86, tickets: 54 },
    { label: "W2", revenue: 92, tickets: 60 },
    { label: "W3", revenue: 110, tickets: 74 },
    { label: "W4", revenue: 124, tickets: 82 },
  ],
};

export default function RevenueDashboard() {
  const [range, setRange] = useState("30d");
  const data = ranges[range as keyof typeof ranges];
  const totalRevenue = useMemo(
    () => data.reduce((sum, item) => sum + item.revenue, 0),
    [data],
  );

  return (
    <div className="min-h-screen bg-slate-50 p-6 text-slate-900">
      <div className="mx-auto max-w-6xl space-y-6">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="mb-2 flex items-center gap-2">
              <Badge variant="outline">Operations</Badge>
              <Badge className="bg-emerald-100 text-emerald-700">
                <TrendingUp className="mr-1 h-3.5 w-3.5" />
                +18.4%
              </Badge>
            </div>
            <h1 className="text-3xl font-semibold tracking-tight">
              Revenue Dashboard
            </h1>
          </div>

          <Select value={range} onValueChange={setRange}>
            <SelectTrigger className="w-[180px] bg-white">
              <SelectValue placeholder="Range" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="7d">Last 7 days</SelectItem>
              <SelectItem value="30d">Last 30 days</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="grid gap-4 md:grid-cols-3">
          {[
            { label: "Revenue", value: `$${totalRevenue}k` },
            { label: "Conversion", value: "6.8%" },
            { label: "Upsell Rate", value: "24%" },
          ].map((metric) => (
            <Card key={metric.label}>
              <CardHeader>
                <CardTitle className="text-sm font-medium text-slate-500">
                  {metric.label}
                </CardTitle>
              </CardHeader>
              <CardContent className="flex items-end justify-between">
                <div className="text-3xl font-semibold">{metric.value}</div>
                <ArrowUpRight className="h-5 w-5 text-emerald-600" />
              </CardContent>
            </Card>
          ))}
        </div>

        <Tabs defaultValue="revenue" className="space-y-4">
          <TabsList className="bg-white">
            <TabsTrigger value="revenue">Revenue</TabsTrigger>
            <TabsTrigger value="tickets">Support tickets</TabsTrigger>
          </TabsList>

          <TabsContent value="revenue">
            <Card>
              <CardHeader>
                <CardTitle>Revenue trend</CardTitle>
              </CardHeader>
              <CardContent className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} />
                    <XAxis dataKey="label" />
                    <YAxis />
                    <Tooltip />
                    <Area
                      dataKey="revenue"
                      stroke="#f97316"
                      fill="#fdba74"
                      fillOpacity={0.35}
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="tickets">
            <Card>
              <CardHeader>
                <CardTitle>Support load</CardTitle>
              </CardHeader>
              <CardContent className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} />
                    <XAxis dataKey="label" />
                    <YAxis />
                    <Tooltip />
                    <Bar
                      dataKey="tickets"
                      fill="#334155"
                      radius={[8, 8, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
```
