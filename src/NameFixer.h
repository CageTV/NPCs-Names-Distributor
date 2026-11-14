#pragma once
namespace NND
{
	namespace NameFixer
	{
		namespace details
		{
			inline bool IsNestedName(std::string_view name) {
				return std::ranges::count(name, '(') > 1 ||
				       std::ranges::count(name, ';') > 1 ||
				       std::ranges::count(name, ',') > 1 ||
				       std::ranges::count(name, '.') > 1 ||
				       std::ranges::count(name, '[') > 1;
			}

			inline bool NeedsFixing(std::string_view name) {
				return name == empty || name == "???" || IsNestedName(name);
			}
		}

		inline bool FixName(RE::Actor* actor) {
			const auto base = actor ? actor->GetActorBase() : nullptr;
			if (!base) {
				return false;
			}
			if (const auto data = actor->extraList.GetExtraTextDisplayData()) {
				if (const auto name = data->GetDisplayName(base, 0)) {
					if (details::NeedsFixing(name)) {
						actor->extraList.Remove(RE::ExtraDataType::kTextDisplayData, data);
						logger::info("{}'s name has been fixed.", base->GetFullName());
						// Immediately refresh the name for NPC we are looking at.
						NND::UpdateCrosshairs();
						return true;
					}
				}
			}
			logger::info("{} does not need a fix.", base->GetFullName());
			return false;
		}

		inline bool FixNameUnsafe(RE::Actor* actor) {
			const auto base = actor ? actor->GetActorBase() : nullptr;
			if (!base) {
				return false;
			}
			if (const auto data = actor->extraList.GetExtraTextDisplayData()) {
				if (const auto name = data->GetDisplayName(base, 0)) {
					actor->extraList.Remove(RE::ExtraDataType::kTextDisplayData, data);
					logger::info("{}'s name has been fixed.", base->GetFullName());
					// Immediately refresh the name for NPC we are looking at.
					NND::UpdateCrosshairs();
					return true;
				}
			}
			logger::info("{} does not need a fix.", base->GetFullName());
			return false;
		}
	}
}
