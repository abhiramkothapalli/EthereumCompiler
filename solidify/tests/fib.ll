; ModuleID = 'fib.cpp'
source_filename = "fib.cpp"
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.13.0"

@candidate_a = global i32 0, align 4
@candidate_b = global i32 0, align 4
@winner = global i32 -1, align 4
@threshold = global i32 10, align 4

; Function Attrs: noinline nounwind ssp uwtable
define i32 @_Z4votei(i32) #0 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = icmp ne i32 %3, 0
  br i1 %4, label %5, label %8

; <label>:5:                                      ; preds = %1
  %6 = load i32, i32* @candidate_b, align 4
  %7 = add nsw i32 %6, 1
  store i32 %7, i32* @candidate_b, align 4
  br label %11

; <label>:8:                                      ; preds = %1
  %9 = load i32, i32* @candidate_a, align 4
  %10 = add nsw i32 %9, 1
  store i32 %10, i32* @candidate_a, align 4
  br label %11

; <label>:11:                                     ; preds = %8, %5
  ret i32 0
}

; Function Attrs: noinline nounwind ssp uwtable
define i32 @_Z10get_winnerv() #0 {
  %1 = load i32, i32* @winner, align 4
  %2 = icmp eq i32 %1, -1
  br i1 %2, label %3, label %8

; <label>:3:                                      ; preds = %0
  %4 = load i32, i32* @candidate_a, align 4
  %5 = load i32, i32* @threshold, align 4
  %6 = icmp sge i32 %4, %5
  br i1 %6, label %7, label %8

; <label>:7:                                      ; preds = %3
  store i32 0, i32* @winner, align 4
  br label %8

; <label>:8:                                      ; preds = %7, %3, %0
  %9 = load i32, i32* @winner, align 4
  %10 = icmp eq i32 %9, -1
  br i1 %10, label %11, label %16

; <label>:11:                                     ; preds = %8
  %12 = load i32, i32* @candidate_b, align 4
  %13 = load i32, i32* @threshold, align 4
  %14 = icmp sge i32 %12, %13
  br i1 %14, label %15, label %16

; <label>:15:                                     ; preds = %11
  store i32 1, i32* @winner, align 4
  br label %16

; <label>:16:                                     ; preds = %15, %11, %8
  %17 = load i32, i32* @winner, align 4
  ret i32 %17
}

attributes #0 = { noinline nounwind ssp uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"PIC Level", i32 2}
!1 = !{!"Apple LLVM version 9.0.0 (clang-900.0.37)"}
