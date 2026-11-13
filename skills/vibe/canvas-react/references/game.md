# Optional Example: Game

Use this for a lightweight toy, score-based interaction, or playful mechanic.

```tsx
import React, { useMemo, useRef, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import type { Mesh } from "three";
import { v4 as uuidv4 } from "uuid";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

const targetColors = ["#22d3ee", "#f97316", "#a78bfa", "#34d399", "#facc15"];

type Target = {
  color: string;
  id: string;
  points: number;
  position: [number, number, number];
};

function FloatingTarget({
  onHit,
  target,
}: {
  onHit: (target: Target) => void;
  target: Target;
}) {
  const meshRef = useRef<Mesh | null>(null);

  useFrame((state) => {
    if (!meshRef.current) return;

    meshRef.current.rotation.x += 0.01;
    meshRef.current.rotation.y += 0.015;
    meshRef.current.position.y =
      target.position[1] +
      Math.sin(state.clock.elapsedTime * 2 + target.points) * 0.15;
  });

  return (
    <mesh
      ref={meshRef}
      position={target.position}
      onClick={(event) => {
        event.stopPropagation();
        onHit(target);
      }}
    >
      <boxGeometry args={[0.9, 0.9, 0.9]} />
      <meshStandardMaterial color={target.color} roughness={0.35} />
    </mesh>
  );
}

export default function OrbitTargetsGame() {
  const targets = useMemo<Target[]>(
    () =>
      targetColors.map((color, index) => ({
        color,
        id: uuidv4(),
        points: index + 1,
        position: [
          (index - 2) * 1.45,
          Math.sin(index) * 0.4,
          index % 2 === 0 ? 0 : -0.7,
        ],
      })),
    [],
  );

  const [score, setScore] = useState(0);
  const [lastHit, setLastHit] = useState<Target | null>(null);

  const hitTarget = (target: Target) => {
    setScore((current) => current + target.points);
    setLastHit(target);
  };

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top,#172554,#020617)] p-6 text-white">
      <div className="mx-auto flex max-w-5xl flex-col gap-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h1 className="text-3xl font-semibold">Orbit Targets</h1>
            <p className="text-sm text-white/60">
              Click floating cubes. Drag to orbit the arena.
            </p>
          </div>
          <div className="flex gap-2">
            <Badge className="bg-white/10 text-white">Score {score}</Badge>
            {lastHit && (
              <Badge className="bg-orange-500/20 text-orange-200">
                Last +{lastHit.points}
              </Badge>
            )}
          </div>
        </div>

        <div className="h-[460px] overflow-hidden rounded-lg border border-white/10 bg-black/30">
          <Canvas camera={{ position: [0, 2.2, 6], fov: 48 }}>
            <ambientLight intensity={0.65} />
            <directionalLight position={[3, 5, 4]} intensity={1.4} />
            <group>
              {targets.map((target) => (
                <FloatingTarget
                  key={target.id}
                  target={target}
                  onHit={hitTarget}
                />
              ))}
            </group>
            <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -1.1, 0]}>
              <circleGeometry args={[4.5, 64]} />
              <meshStandardMaterial color="#0f172a" roughness={0.8} />
            </mesh>
            <OrbitControls enablePan={false} maxDistance={8} minDistance={4} />
          </Canvas>
        </div>

        <div className="flex justify-end">
          <Button variant="outline" onClick={() => setScore(0)}>
            Reset score
          </Button>
        </div>
      </div>
    </div>
  );
}
```
