using UnityEngine;

namespace QuantumDefender
{
    /// <summary>Phase 1 tunables mirrored from web reference constants where gameplay parity requires it.</summary>
    public static class QuantumStateConstants
    {
        public const float QuaternionTolerance = 0.9f;
        public const float GyroSpeedBoost = 1.2f;
        public const float BaseAutoTargetSpeed = 30f;
        public const float IdleTimeoutMs = 6000f;
        public const float TargetLockBaseSpeed = 6f;
        public const float TargetLockQuickLockSpeedBoost = 2f;
        public const float TargetLockGyroSpeedBoost = 3f;
        public const float TargetLockIdleTimeoutMs = 350f;
        public const float FireAnimationDuration = 4f;
        public const float PulseWaveExpandDuration = 32f;

        public const float Rc = 0.57735026919f;
        public const float Tau = 0.03464101615f;
        public const int StandingWavePointsPerShell = 65;
        public const int CriticalSpherePointCount = 800;
        public const float CriticalShellSkipTolerance = 0.001f;
        public const float StandingWaveDimFactor = 0.2f;
        public const float ShellRotationDefaultAnimationSpeed = 0.55f;
        public const float ShellRotationBaseSpeedMultiplier = 0.75f;
        public const float StandingWaveRotationMultiplier = ShellRotationBaseSpeedMultiplier;
        public const float ShellRotationInnerProfileMinSpeed = 0.2f;
        public const float ShellRotationInnerProfileMaxSpeed = 2.0f;
        public const float ShellRotationOuterProfileMinSpeed = 0.2f;
        public const float ShellRotationOuterProfileMaxSpeed = 2.0f;

        public static readonly float[] ShellAs =
        {
            0.92f, 0.78f, 0.64f, 0.52f, 0.50f, 0.48f, 0.36f, 0.22f, 0.00f, -0.30f
        };

        public const int ShellCount = 10;
        public const float GoldenRatio = 1.61803398875f;
        private static readonly int[] AllRenderedShellIndices = { 0, 1, 2, 3, 5, 6, 7, 8, 9 };

        private static readonly int[][] LevelShellIndexProfiles =
        {
            new[] { 2, 3, 5, 6 },
            new[] { 2, 3, 5, 6 },
            new[] { 2, 3, 5, 6 },
            new[] { 1, 2, 3, 5, 6 },
            new[] { 1, 2, 3, 5, 6, 7 },
            new[] { 0, 1, 2, 3, 5, 6, 7 },
            new[] { 0, 1, 2, 3, 5, 6, 7, 8 },
            AllRenderedShellIndices
        };

        public static float ShellRadius(float a)
        {
            return Mathf.Sqrt(1f - a * a) / (1f + a);
        }

        public static bool IsCriticalShell(float radius)
        {
            return Mathf.Abs(radius - Rc) < CriticalShellSkipTolerance;
        }

        public static int[] GetShellIndicesForLevel(int level)
        {
            if (level <= 0)
            {
                return (int[])AllRenderedShellIndices.Clone();
            }

            var profileIndex = Mathf.Min(level, LevelShellIndexProfiles.Length) - 1;
            return (int[])LevelShellIndexProfiles[profileIndex].Clone();
        }

        public static float CalculateOutermostVisibleShellRadiusForLevel(int level)
        {
            var indices = GetShellIndicesForLevel(level);
            var maxRadius = 0f;
            for (var i = 0; i < indices.Length; i++)
            {
                var sourceIndex = indices[i];
                if (sourceIndex < 0 || sourceIndex >= ShellAs.Length)
                {
                    continue;
                }

                maxRadius = Mathf.Max(maxRadius, ShellRadius(ShellAs[sourceIndex]));
            }

            return maxRadius;
        }

        public static float StandingWaveAmplitude(Vector3 initialPosition, int mode)
        {
            if (mode <= 0)
            {
                return 1f;
            }

            var rHat = initialPosition.normalized;
            var phiLoc = mode * Mathf.PI * Vector3.Dot(Vector3.forward, rHat);
            return Mathf.Abs(Mathf.Cos(phiLoc));
        }
    }
}
