; ModuleID = 'sample.cpp'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: uwtable
define i32 @_Z3fibi(i32 %n) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 %n, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = icmp sle i32 %3, 1
  br i1 %4, label %5, label %7

; <label>:5                                       ; preds = %0
  %6 = load i32, i32* %2, align 4
  store i32 %6, i32* %1, align 4
  br label %15

; <label>:7                                       ; preds = %0
  %8 = load i32, i32* %2, align 4
  %9 = sub nsw i32 %8, 1
  %10 = call i32 @_Z3fibi(i32 %9)
  %11 = load i32, i32* %2, align 4
  %12 = sub nsw i32 %11, 2
  %13 = call i32 @_Z3fibi(i32 %12)
  %14 = add nsw i32 %10, %13
  store i32 %14, i32* %1, align 4
  br label %15

; <label>:15                                      ; preds = %7, %5
  %16 = load i32, i32* %1, align 4
  ret i32 %16
}

; Function Attrs: norecurse uwtable
define i32 @main() #1 {
  %1 = alloca i32, align 4
  %n = alloca i32, align 4
  %a = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 9, i32* %n, align 4
  %2 = call i32 @_Z3fibi(i32 9)
  store i32 %2, i32* %a, align 4
  %3 = load i32, i32* %a, align 4
  ret i32 %3
}

attributes #0 = { uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { norecurse uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
